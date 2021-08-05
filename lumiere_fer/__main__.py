from lumiere_fer.evaluators.evaluate_ck_plus import evaluate_on_ck_plus
from lumiere_fer.evaluators.evaluate_fer_2013 import evaluate_on_fer_2013


def main():
    ck_plus_evaluation_result = evaluate_on_ck_plus()
    print('The Evaluation Result for CK Plus is: ')
    print(
        ck_plus_evaluation_result.readable_string(),
    )

    fer_2013_evaluation_result = evaluate_on_fer_2013()
    print('The Evaluation Result for FER 2013 is: ')
    print(
        fer_2013_evaluation_result.readable_string(),
    )


if __name__ == '__main__':
    main()
