class Podcast:
    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link
        self.episodes = []
    
    def __str__(self):
        return(f"{self.title}\n{self.description}\n{self.link}")

    def add_episode(self, episode):
        self.episodes.append(episode) 
    
    def to_dict(self):
        return{
                "title": self.title,
                "description": self.description,
                "link": self.link,
                "episodes": [episode.to_dict() for episode in self.episodes]
                }
    

class Episode:
    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link

    def __str__(self):
        return (f"{self.title}\n{self.description}\n{self.link}")
        
    def to_dict(self):
        return{
                "title": self.title,
                "description": self.description,
                "link": self.link
                }
