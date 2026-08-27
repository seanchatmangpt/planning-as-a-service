import unittest

from project2_admission import Admission, AdmissionRefused, admit_project2_subject

BASE = "f05534b0df81bb3fccf48209355fd6d20498fbbc"
HEAD = "0123456789abcdef0123456789abcdef01234567"


class Project2AdmissionTests(unittest.TestCase):
    def test_exact_subject_has_deterministic_receipt(self):
        subject = Admission(
            repo="seanchatmangpt/planning-as-a-service",
            base=BASE,
            head=HEAD,
            authority="SELECT|CONSTRUCT|VERIFY",
        )
        self.assertEqual(admit_project2_subject(subject), admit_project2_subject(subject))
        self.assertEqual(len(admit_project2_subject(subject)), 64)

    def test_non_exact_subject_is_refused(self):
        with self.assertRaisesRegex(AdmissionRefused, "REFUSED_NON_EXACT_SUBJECT"):
            admit_project2_subject(
                Admission(
                    repo="seanchatmangpt/planning-as-a-service",
                    base="main",
                    head=HEAD,
                    authority="SELECT|CONSTRUCT|VERIFY",
                )
            )

    def test_ambient_do_is_refused(self):
        with self.assertRaisesRegex(AdmissionRefused, "REFUSED_AMBIENT_DO_AUTHORITY"):
            admit_project2_subject(
                Admission(
                    repo="seanchatmangpt/planning-as-a-service",
                    base=BASE,
                    head=HEAD,
                    authority="SELECT|CONSTRUCT|VERIFY",
                    direct_actuation=True,
                )
            )


if __name__ == "__main__":
    unittest.main()
