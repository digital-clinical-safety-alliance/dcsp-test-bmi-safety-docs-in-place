""" BMI calculator """


class BMICalculator:
    def __init__(self):
        """Initialise the BMI test class

        Initialisation of the test class

        Hazards:
            WrongPatient (1): The wrong patient (testing)
            WrongPatient (2): The wrong patient (testing)
        """
        pass

    def BMI(self, weight: float, height: float) -> float:
        """Work out BMI from weight

        Calculate the weight of the patient. Uses metric units

        Args:
            weight (float): weight of the patient in kilograms
            height (float): height of the patient in meters

        Returns:
            float: BMI of the patient

        Raises:
            ValueError: wrong weight range
            ValueError: wrong height range

        Hazards:
            WrongPatient (1): The wrong patient
            WrongDemograhics (2): The wrong patient gender
        """
        if not self.weight_check(weight):
            raise ValueError("Weight is out of range")

        if not self.height_check(height):
            raise ValueError("Height is out of range")

        BMI: float = weight / ((height / 100) * (height / 100))

        return BMI

    def weight_check(self, weight: float) -> bool:
        """Check that a logical weight has been used

        Args:
            weight (float): weight in kilograms.

        Returns:
            bool: True if a valid weight.

        Hazards:
            WrongObservationResult (3): wrong weight entered.
            WrongObservationResult (4): wrong weight entered.
        """
        if weight > 200 or weight < 1:
            return False

        return True

    def height_check(self, height: float) -> bool:
        """Check that a logical height has been used

        Args:
            height (float): height in cm.

        Returns:
            bool: True if a valid height.

        Hazards:
            WrongObservationResult (4): wrong height entered.
            WrongObservationResult (5): wrong weight entered.
        """
        if height > 300 or height < 1:
            return False

        return True
