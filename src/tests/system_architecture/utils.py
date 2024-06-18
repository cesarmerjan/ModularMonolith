# mypy: ignore-errors
import ast
import os
from collections import defaultdict
from dataclasses import asdict, dataclass
from typing import Optional

from src.settings import ROOT_DIRECTORY, SHARED_MODELES_NAMES

SRC_PATH = os.path.join(ROOT_DIRECTORY, "src/")


@dataclass
class ImportDataStructure:
    module: list[Optional[str]]
    name: str
    alias: Optional[str]

    def to_dict(self) -> dict:
        return asdict(self)


def get_imports_from_module(path_to_module: str) -> list[Optional[ImportDataStructure]]:
    with open(path_to_module) as fh:
        root = ast.parse(fh.read(), path_to_module)

    module_imports: list[Optional[ImportDataStructure]] = []
    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.Import):
            module: list = []
            for n in node.names:
                module_imports.append(ImportDataStructure(module, n.name, None))
        elif isinstance(node, ast.ImportFrom):
            module_parts: list[Optional[str]] = node.module.split(".")
            for n in node.names:
                module_imports.append(
                    ImportDataStructure(module_parts, n.name, n.asname)
                )
    return module_imports


def get_system_domains(src_path: str) -> list[str]:
    system_domains = [
        element
        for element in os.listdir(src_path)
        if os.path.isdir(os.path.join(src_path, element))
    ]
    return system_domains


def get_domain_modules(
    src_path: str, system_domains: list[str]
) -> dict[str, list[str]]:
    domain_modules = defaultdict(list)
    for domain in system_domains:
        for dir_path, dir_names, file_names in os.walk(os.path.join(src_path, domain)):
            for file_name in file_names:
                if file_name.lower().endswith(".py"):
                    domain_modules[domain].append(os.path.join(dir_path, file_name))
    return domain_modules


def get_modules_that_do_not_respect_the_system_architecture(
    domain_modules: dict[str, list[str]]
) -> dict[str, list[ImportDataStructure]]:

    modules_that_do_not_respect_the_system_architecture = defaultdict(list)
    for domain, domain_modules_path_list in domain_modules.items():

        allowed_domain_imports = ("_shared", "settings", domain)

        for domain_modules_path in domain_modules_path_list:

            module_imports = get_imports_from_module(domain_modules_path)

            for import_data_structure in module_imports:
                if import_data_structure.module:
                    if import_data_structure.module[0] == "src":
                        if (
                            import_data_structure.module[1]
                            not in allowed_domain_imports
                        ):
                            import_name = import_data_structure.name
                            last_model_import = import_data_structure.module[-1]

                            if all(
                                [
                                    import_name not in SHARED_MODELES_NAMES,
                                    last_model_import not in SHARED_MODELES_NAMES,
                                ]
                            ):
                                modules_that_do_not_respect_the_system_architecture[
                                    domain_modules_path
                                ].append(import_data_structure)

    return modules_that_do_not_respect_the_system_architecture


def check_system_architecture() -> None:
    modules_that_do_not_respect_the_system_architecture = (
        get_modules_that_do_not_respect_the_system_architecture(
            get_domain_modules(
                SRC_PATH,
                get_system_domains(SRC_PATH),
            )
        )
    )

    if modules_that_do_not_respect_the_system_architecture:
        message = ""
        for (
            module,
            module_imports,
        ) in modules_that_do_not_respect_the_system_architecture.items():
            message += f"\nFile: {module}\n"
            for import_data_structure in module_imports:
                if import_data_structure.module:
                    message += f"  Module: {'.'.join(import_data_structure.module)}"
                message += f"  Name: {import_data_structure.name}\n"

        raise Exception(message)
