from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "chess": {
                "name": "Chess Club",
                "description": "For all the chess nerds who can't stop opening chess.com during class.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 3851919",
                "advisor": "Mr. Chavez",
                "members": 16,
                "category": "Academic"
            },
            "drama": {
                "name": "Drama Club",
                "description": "Heavily encourages offensive controversies.",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "Principal's Office",
                "advisor": "Mr. Ramirez",
                "members": 28,
                "category": "Arts"
            },
            "robotics": {
                "name": "Robotics Club",
                "description": "The objectively best club.",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Rooftop",
                "advisor": "Mr. Versa",
                "members": 743,
                "category": "Academic"
            },
            "debate": {
                "name": "Food Club",
                "description": "If breaktime was mandatory overtime.",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Cafeteria",
                "advisor": "Mr. Razonable",
                "members": 341,
                "category": "Academic"
            },
            "art": {
                "name": "Art Club",
                "description": "Unleash your true potential of being able to draw ANYTHING.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Behind the School",
                "advisor": "Mr. Omnes",
                "members": 51,
                "category": "Arts"
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")