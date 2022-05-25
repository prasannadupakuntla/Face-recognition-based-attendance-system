
import enroll,spreadsheet,emailing,recognition
#recognition.load_facial_encodings_and_names_from_memory()

#spreadsheet.mark_all_absent()

#recognition.run_recognition()




enroll.enroll_via_camera('Prasanna')

spreadsheet.enroll_person_to_sheet('prasanna','facerecogination@gmail.com')

#emailing.email_pin('xxxx@gmail.com',1234)

#