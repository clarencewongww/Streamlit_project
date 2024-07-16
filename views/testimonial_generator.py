import streamlit as st
import anthropic
import hmac

# Check password
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["simple_pass"]):
            st.session_state["sim_password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["sim_password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("sim_password_correct", False):
        return True

    # Show input for password.
    st.success("This tool helps to generate testimonal based on your input.")
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect.")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Main Streamlit app starts here
# Define parameters
MODEL = "claude-3-haiku-20240307"
API_KEY = st.secrets["ANTHROPIC_API_KEY"]
SYSTEM = """
You are a teacher/educator that is writing testimonial for students that are leaving the school at secondary 4 or 5 in Singapore. 
Make use of the inputs given to write a 5 paragraph testimonial for the student. Each paragraph should be 300 words. Total 1500 words. 
Emphasize on the acheivements and examples but never make up examples that are not stated. If needed, you can give generic statements. 
Do not have any other statement or words besides the testimonial, no header, no title. \n
Examples of some testimonial: \n
1. \n
[Name] was a student of [School] from [Year] to [Year].

[Name] is a well-mannered student who is continually striving to improve her academic performance. She consciously tries to upgrade herself and gives her best effort so as to realise her full potential. With her hard work, she obtained Top in Standard in both Secondary 1 and Secondary 3. She works in a determined fashion and she likes to challenge herself to do better each time. She has been awarded the Edusave Scholarship for Secondary School for three consecutive years. [Name] is proactive in seeking feedback and ways to improve. She is able to command the attention of her peers through her confidence and good public speaking skills.

[Name] kept a good balance between academic work and her Co-Curricular Activities (CCA), participating fully in the school activities and programmes. [Name] was part of the Dance team that represented the school in the Singapore Youth Festival where they won the Merit Award. She took her trainings seriously and encouraged her teammates when they were feeling tired or lost in their dance practices.

Apart from that, [Name] was also an [ROLE] of the [LEADERSHIP]. With her fellow peers, she organised several Value-In-Actions events like the fundraising for the President’s Challenge where she took charge of the budgeting and logistics. She exhibited good leadership qualities when taking on tasks assigned to her and she delegated work in a fair manner, making her a popular leader in the committee. [Name] also ensured that she gave her juniors timely check-ins on their well-being to motivate them to give their best. Under her team’s guidance, the PSL led the school to enter the Singapore Book of Records for the most number of people writing on ice cream sticks at the same time and the largest ice cream stick bomb.

Being friendly and helpful, [Name] was respected by her peers and tutors alike. She accepted feedback readily and was responsive to giving and receiving ideas. [Name] was also generous and patient towards her classmates by giving them academic and emotion support. 
[Name] has indeed demonstrated the qualities needed for success in life. These qualities will stand her in good stead in her future endeavours.

2. \n
[Name] was a student of [School] from [Year] to [Year].

[Name] displays a lively intelligence and has a practical approach to life. He is also a bright and resourceful student. A fast learner, he grasps concepts easily. He is not afraid to assert his opinions with great reasoning power and persuasive arguments. Where his studies are concerned, he sees setbacks as opportunities for him to improve and upgrade himself further. When in doubt, he is never afraid to consult his classmates as well as his teachers. This has allowed him to obtain Edusave Good Progress Award in Secondary 2 as well as Edusave Scholarship for Secondary School in Secondary 3.

[Name] also possesses the ability to remain calm and collected during stressful situations such as those due to the demands of competitions and studies. He was selected to represent the school in the MOE History Challenge in 2021 due to his confidence in expressing his views and high aptitude for History. As a student of diverse interests, [Name] and his team wowed the judges with their fusion dish and clinched the first prize in the Temasek Polytechnic ‘Future of Food’ Baking Challenge in 2020. [Name] is an avid cyclist and made it to the top 10 for both of the cycling competitions he participated in [Year] organised by the Singapore Cycling Federation. 
[Name] was a dedicated member of the National Police Cadet Corps (NPCC). His persevering and resilient nature was evident in his commitment during the physically demanding practice sessions. He was a non-Commissioned Officer who stepped into the role of a squad instructor and precision drill squad instructor with ease. He guided and taught his juniors on executing foot drills and baton drills. He also created a choreography using the model rifle for a school event. Despite his busy schedule, [Name] was able to take on leadership role as a Young Ambassor in [Year] to 2021 where he led the juniors in planning and executing the Post Exam Activities and Racial Harmony Day celebration as an Executive Committee Member. 

[Name] is a problem solver and his creativity together with his tenacity will augur well for him and he certainly can carve out a successful future for himself if he puts his mind into what he wants to do.

3. \n
[Name] was a student of [School] from [Year] to [Year].

[Name] is a well-mannered and respectful person. He is also an active and diligent student who has the potential for greater achievements. He is someone who would rise to the occasion and overcome any challenges. [Name] is also a good team player. During group discussions, he never fails to participate actively and ensures that the group tasks are completed successfully. He also does not allow setbacks to deter him from striving to attain these goals. When given constructive feedback regarding his academic subjects, he accepts it positively and tries to put into practice what has been recommended to him. 

[Name] was the Captain of the school Track and Field team. He led by example and contributed to his Co-Curricular Activity (CCA) by participating in many activities and competitions. He took part in the 400m, 800m running events and the 4X400m relay race where he came in Third during heats in the National School Games [Year]. He also participated in the National Cross Country Championship where he was placed 88th out of over 300 competitors. He showed dedication and commitment to the activities conducted by his CCA and he served as a role model for his juniors. 

[Name] proved to be a capable leader. He held a key appointment in the Executive Committee of the Peer Support Leaders. He guided his juniors in handling school-wide events like Mental Health Week and Sec 1 Orientation where they improved the general well-being of the student population. [Name] could be trusted with responsibilities to ensure that the events run smoothly and he could pre-empt any possible issues that may arise.

[Name] exhibited compassion in his character as he was involved in the many school charity events. One of the student initiated Values-in-Action events that he participated in was to send simple workout videos and encouraging words in four different languages to the elderly to brighten up their day. 

Being a mature and independent boy, [Name] is focussed and single-minded about achieving his goals even when he faced difficulties. He pursues his interests with purpose and enthusiasm. He also takes his responsibilities seriously and he can be entrusted with a task and be assured of a positive outcome. He is also polite and respectful of authority and interacts well with his peers. [Name] will be an asset to any organisation that he decides to associate with in the future.


        """

# Anthropic Client
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=API_KEY,
)

# Attribute section with columns
st.header("Type in the attributes")
# Set columns for input
col1, col2 = st.columns([2,2])
col3, col4 = st.columns([2,2])
# columns 
with col1:
    stu_name = st.text_input('Enter the name of student:')
with col2:
    stu_lead = st.text_input('Enter some comments of student\'s leadership:')
with col3:
    stu_cca = st.selectbox("Select CCA of student:", ("Badminton", "Scouts", "NCC", "Basketball", "Drama"), index = None, placeholder="Select CCA...")
with col4:
    stu_att = st.text_input("Enter some comments on student's learning attitude:")


def generate_testimonial():

    testimonial_placeholder = st.empty() 
    full_testimonial = ""   

    with client.messages.stream(
        model=MODEL,
        max_tokens=4096,
        system = SYSTEM,
        messages=[
            {"role": "user", "content": f"Student name is {stu_name}, with leadership in {stu_lead} and has learning attitude of {stu_att}. He/she is from the Co-curricula activity of {stu_cca}."}
        ]
    ) as stream: 
        for text in stream.text_stream:
                full_testimonial += text
                testimonial_placeholder.markdown(full_testimonial)

if st.button("Generate Testimonial"):
        # Check if all mandatory fields are filled
    if not stu_name or not stu_att or not stu_cca or stu_lead is None:
        st.error("Please fill in all the mandatory fields.")
    else:
        generate_testimonial()
   