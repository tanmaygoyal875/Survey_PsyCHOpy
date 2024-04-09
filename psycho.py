import csv
import os.path
import time
from psychopy import visual, core, event, gui

# Define questions and correct answers
questions = ["Write this word as is: bird", "Write this word as is: bicycle", "Write this word as is: chocolately", "Baanna", "Husabnd","Oouctps","Lbiarry","Aeudvntre","Lnadascpe","Chcoltoaey","Gtuiar","Baeskt","Pruple","Rsoe", "Moon", "Hnad" ,"Snad"]
correct_answers = ["bird", "bicycle", "chocolately","banana","husband","octopus","library","adventure","landscape","chocolaty","guitar","basket","purple","rose","moon","hand","sand"]

# Set up PsychoPy window
win = visual.Window(size=(800, 600), units='pix', fullscr=False)
# Set up text stimuli
text_stim = visual.TextStim(win, text='', color='black')

# Instructions
instructions_text = "Press Enter to start the quiz. write the correct word for given jumbled ones and press Enter to submit your response."
instructions = visual.TextStim(win, text=instructions_text, color='black')
instructions.draw()
win.flip()

# Wait for Enter to start the quiz
event.waitKeys(keyList=['return'])

# Check if CSV file exists
csv_file_path = r"C:\Users\Tanish Goyal\Desktop\hs202\participant_responses.csv"
file_exists = os.path.isfile(csv_file_path)

# Initialize list to store participant responses
participant_responses = []

# If the CSV file exists, load existing participant responses
if file_exists:
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            participant_responses.append(row)

# Determine the participant number
participant_number = len(participant_responses) + 1

# Loop through questions
participant_data = [f"Participant {participant_number}"]
for i, question in enumerate(questions):
    # Display question
    text_stim.text = question
    text_stim.draw()
    win.flip()

    # Start time for current question
    start_time = time.time()

    # Create a text box for participant response
    response_box = gui.Dlg(title="Question")
    response_box.addField('Answer:')
    response_box.show()

    if not response_box.OK:
        core.quit()  # Quit if participant closes the response box

    response_text = response_box.data[0].lower()  # Get response and convert to lowercase

    # Record response time
    response_time = time.time() - start_time

    # Check answer correctness
    correct = response_text == correct_answers[i]

    # Append participant response to participant_data
    participant_data.extend([response_text, response_time, correct])

# Append participant_data to participant_responses
participant_responses.append(participant_data)

# End of quiz
end_text = "End of quiz. Thank you for participating!"
end_stim = visual.TextStim(win, text=end_text, color='black')
end_stim.draw()
win.flip()
core.wait(2)

# Save participant responses to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for response_data in participant_responses:
        writer.writerow(response_data)

# Close PsychoPy window
win.close()
core.quit()





#FINAL CODE
