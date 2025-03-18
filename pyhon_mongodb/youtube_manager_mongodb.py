from pymongo import MongoClient
from bson import objectid

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.d6x2u.mongodb.net/", tlsAllowInvalidCertificates = True, serverSelectionTimeoutMS=5000)

db = client["ytmanager"]
video_collection = db["video"]

print(video_collection)

def add_video(name,time):
     video_collection.insert_one({"name": name, "time": time})
     print(f"Video '{name}' added successfully!")


def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")


def update_video(video_id,updated_name,updated_time):
    video_collection.update_one(
        {"id": objectid (video_id)},
        {"$set": {"name":updated_name, "time":updated_time}}
    )


def delete_video(video_id):
    video_collection.delete_one({"_id": objectid (video_id)})
    





def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all video")
        print("2. Add a new video")
        print("3. update a video")
        print("4. delete a video")
        print("5. Exit the App")
        choice = input("Enter your choice:")

        if choice == "1":
            list_video()

        elif choice == "2":
            name = input("please enter vedio tittle")
            time = input("please enter vedio duration")
            add_video(name,time)

        elif choice == "3":
            vedio_id = input("please enter the vedio id")
            name = input("please enter updated vidio tittle")
            time = input("please enter updated video duration")
            update_video(vedio_id,name,time)

        elif choice == "4":
            vedio_id = input("please enter the vedio id")
            delete_video(vedio_id)

        elif choice == "5":
            break

        else:
            print("invalid choice")

    

if __name__ == "__main__":
    main()