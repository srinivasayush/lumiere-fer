from lumiere_fer.constants.generic import DATASETS_TO_PATHS
from lumiere_fer.evaluators.evaluate_on_images import evaluate_on_images
from lumiere_fer.utils.file import write_file


def main():
    detectors = input('Please enter the detectors split by space(e.g "opencv dlib mtcnn"): ').replace('"', '').split(' ')

    for detector in detectors:
        for dataset_name, image_filepaths in DATASETS_TO_PATHS.items():
            print(f'Evaluating model on {dataset_name}')

            dataset_evaluation_result = evaluate_on_images(
                detector=detector,
                image_filepaths=image_filepaths,
                verbose=True,
            )

            print(f'The Evaluation Result for {dataset_name} with detector {detector} is: ')
            print(dataset_evaluation_result)

            write_file(
                filepath=f'./results/{detector}_{dataset_name}_results.json',
                content=str(dataset_evaluation_result),
                overwrite=True,
                append=False,
            )


if __name__ == '__main__':
    main()
