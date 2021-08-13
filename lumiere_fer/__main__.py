from typing import ContextManager
from lumiere_fer.utils.file import write_file
from lumiere_fer.evaluators.evaluate_ck_plus import evaluate_on_ck_plus
from lumiere_fer.evaluators.evaluate_fer_2013 import evaluate_on_fer_2013
import json


def main():
    detectors = input('Please enter the detectors split by space(e.g "opencv mtcnn"): ').replace('"', '').split(' ')

    for detector in detectors:
        print(f'Using detector {detector}')
        print('Evaluating model on CK Plus...')
        ck_plus_evaluation_result = evaluate_on_ck_plus(
            detector=detector,
        )
        print(f'The Evaluation Result for CK Plus with detector {detector} is: ')
        print(ck_plus_evaluation_result)

        write_file(
            filepath=f'./results/{detector}_ckplus_results.json',
            content=str(ck_plus_evaluation_result),
            overwrite=True,
            append=False,
        )

        print('Evaluating model on FER 2013...')
        fer_2013_evaluation_result = evaluate_on_fer_2013(
            detector=detector,
        )
        print(f'The Evaluation Result for FER 2013 with detector {detector} is: ')
        print(fer_2013_evaluation_result)

        write_file(
            filepath=f'./results/{detector}_fer2013_results.json',
            content=str(fer_2013_evaluation_result),
            overwrite=True,
            append=False,
        )


if __name__ == '__main__':
    main()
