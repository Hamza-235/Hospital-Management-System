class Patient:
    def __init__(self,name,severity):
        self.name=name
        self.severity=severity
class priority_queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
       return len(self.queue)==0
    def enqueue(self,patient):
        self.queue.append(patient)
        self.queue.sort(key=lambda x:x.severity,reverse=True)
    def dequeue(self):
        if self.is_empty():
            print("queue is empty ")    
        return self.queue.pop(0)
    def display(self):
        if self.is_empty():
            print("queue is empty")
        else :
           for patient in self.queue:
               print(f" Name of patient {patient.name}, severity of patient {patient.severity}")

class HospitalManagementSystem:
    def __init__(self):
        self.patient_queue=priority_queue()
    def add_patient(self,name,severity):
        patient=Patient(name,severity)
        self.patient_queue.enqueue(patient)
        print(f"Patient {name} added to the queue with severity {severity}.")

    def attend_patient(self):
        self.patient_queue.dequeue()
    
    def display_patients(self):
        self.patient_queue.display()
 
if __name__ == "__main__":
    hms = HospitalManagementSystem()

    # Add patients
    hms.add_patient("Alice", 5)
    hms.add_patient("Bob", 3)
    hms.add_patient("Charlie", 8)
    hms.add_patient("Diana", 2)

    # Display patients
    print("\nCurrent patient queue:")
    hms.display_patients()

    # Attend patients
    print("\nAttending to patients:")
    hms.attend_patient()
    hms.attend_patient()

    # Displaying remaining patients
    print("\nRemaining patient queue:")
    hms.display_patients()
