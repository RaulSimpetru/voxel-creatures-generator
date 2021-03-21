import os
from typing import Optional, List, Literal

import numpy as np

import utils.representation as rep


def make_data(
    n: int,
    input_dir: str,
    output_dir: Optional[str] = None,
    *,
    only_uniques: bool = False,
    save_option: Literal["pickles", "objs"] = "objs",
):
    rep.sort_files_in_dirs(input_dir)

    if save_option == "pickles":
        rep.abstract_reps_to_pickles(
            rep.dict_reps_to_abstract_reps(rep.make_random_creatures(n, input_dir, only_uniques=only_uniques)),
            output_dir=output_dir,
        )

        return

    if save_option == "objs":
        rep.dict_reps_to_objs(
            rep.abstract_reps_to_dict_reps(
                rep.correct_abstract_reps_for_display(
                    rep.dict_reps_to_abstract_reps(rep.make_random_creatures(n, input_dir, only_uniques=only_uniques))
                )
            ),
            output_dir=output_dir,
        )

        return

    raise ValueError('"save_option" must be either "pickles" or "objs"!')


def make_random_outputs(n: int) -> List[np.ndarray]:
    return [np.random.choice([0, 1], size=rep.STANDARD_SHAPE, p=[0.875, 0.125]).astype(np.float32) for _ in range(n)]


def pick_random_data(input_dir: str, output_dir: str, f_name: str, *, to_display: bool = False):
    temp = rep.pickles_to_abstract_reps(input_dir, files_to_convert=[*np.random.choice(os.listdir(input_dir), 1)])

    rep.dict_reps_to_objs(
        rep.abstract_reps_to_dict_reps(rep.correct_abstract_reps_for_display(temp) if to_display else temp),
        output_dir=output_dir,
        output_name=f_name,
    )
