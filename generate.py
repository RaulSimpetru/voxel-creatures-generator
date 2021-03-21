import argparse
import os
import sys
from pathlib import Path

from utils.data import make_data
from utils.representation import FUNCTIONS_DICT

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate some creatures")

    parser.add_argument("-n", "--nrOfCreatures", default=100, type=int, help="how many creatures to create")
    parser.add_argument("-i", "--input", type=str, required=True, help="input path")
    parser.add_argument("-o", "--output", type=str, required=True, help="output path")
    parser.add_argument(
        "-u",
        "--uniques",
        action="store_const",
        const=True,
        default=False,
        help="if only unique creatures should be generated",
    )

    n, input_dir, output_dir, only_uniques = vars(parser.parse_args()).values()

    if not any([Path.exists(Path(input_dir)), Path.exists(Path(output_dir))]):
        Path.mkdir(Path(input_dir), parents=False, exist_ok=True)
        Path.mkdir(Path(output_dir), parents=False, exist_ok=True)

        for dir_name in [*FUNCTIONS_DICT.values(), "body"]:
            Path.mkdir(Path(input_dir, dir_name), exist_ok=True)

        print(
            "\nCreated input and output dirs.\n\nPlease put your data in the input dir.\n"
            "The data will be auto sorted the next time you run this script"
        )

        sys.exit()

    # make sure the output dir is empty
    for file in os.scandir(output_dir):
        os.remove(file.path)

    make_data(
        n=n,
        input_dir=input_dir,
        output_dir=output_dir,
        only_uniques=only_uniques,
    )
