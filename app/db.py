from app.models.CourseModel import CourseModel
from app.models.UserCommentModel import UserCommentModel
from app.models.UserModel import UserModel


# ============================================================
# Course Database
# ============================================================

CourseDB: list[CourseModel] = [
    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440001",
        "title": "Python Fundamentals",
        "subtitle": "Learn Python from the ground up",
        "description": "A complete beginner-friendly course covering Python fundamentals, syntax, functions, and basic programming concepts.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440001",
        "price": 999.00,
        "discount_price": 799.00,
        "thumbnail": "https://example.com/python.jpg",
        "promovideo": "https://example.com/python-video",
        "difficalulty_level": "beginner",
        "total_duration_in_seconds": 28800,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440002",
        "title": "Advanced Python",
        "subtitle": "Master advanced Python programming",
        "description": "Learn advanced Python concepts including decorators, generators, context managers, and asynchronous programming.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440002",
        "price": 1499.00,
        "discount_price": 1199.00,
        "thumbnail": "https://example.com/advanced-python.jpg",
        "promovideo": "https://example.com/advanced-python-video",
        "difficalulty_level": "advanced",
        "total_duration_in_seconds": 43200,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440003",
        "title": "FastAPI Development",
        "subtitle": "Build modern APIs with FastAPI",
        "description": "Learn how to build production-ready REST APIs using FastAPI, Pydantic, validation, dependencies, and routing.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440003",
        "price": 1299.00,
        "discount_price": 999.00,
        "thumbnail": "https://example.com/fastapi.jpg",
        "promovideo": "https://example.com/fastapi-video",
        "difficalulty_level": "intermediate",
        "total_duration_in_seconds": 36000,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440004",
        "title": "Database Design",
        "subtitle": "Learn SQL and database design",
        "description": "Understand relational databases, SQL queries, normalization, indexes, relationships, and database design principles.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440004",
        "price": 1099.00,
        "discount_price": 899.00,
        "thumbnail": "https://example.com/database.jpg",
        "promovideo": "https://example.com/database-video",
        "difficalulty_level": "intermediate",
        "total_duration_in_seconds": 32400,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440005",
        "title": "Git and GitHub",
        "subtitle": "Learn version control properly",
        "description": "Learn Git commands, branching, merging, pull requests, remote repositories, and collaborative development workflows.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440005",
        "price": 599.00,
        "discount_price": 399.00,
        "thumbnail": "https://example.com/git.jpg",
        "promovideo": "https://example.com/git-video",
        "difficalulty_level": "beginner",
        "total_duration_in_seconds": 18000,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440006",
        "title": "React Development",
        "subtitle": "Build modern frontend applications",
        "description": "Learn React components, hooks, state management, routing, forms, and modern frontend development practices.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440006",
        "price": 1399.00,
        "discount_price": 1099.00,
        "thumbnail": "https://example.com/react.jpg",
        "promovideo": "https://example.com/react-video",
        "difficalulty_level": "intermediate",
        "total_duration_in_seconds": 39600,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440007",
        "title": "Docker Basics",
        "subtitle": "Containerize your applications",
        "description": "Learn Docker images, containers, volumes, networks, Dockerfiles, and basic container deployment workflows.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440007",
        "price": 899.00,
        "discount_price": 699.00,
        "thumbnail": "https://example.com/docker.jpg",
        "promovideo": "https://example.com/docker-video",
        "difficalulty_level": "beginner",
        "total_duration_in_seconds": 21600,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440008",
        "title": "AWS Cloud Basics",
        "subtitle": "Introduction to cloud computing",
        "description": "Understand AWS fundamentals, EC2, S3, IAM, networking, and the basics of deploying applications to the cloud.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440008",
        "price": 1599.00,
        "discount_price": 1299.00,
        "thumbnail": "https://example.com/aws.jpg",
        "promovideo": "https://example.com/aws-video",
        "difficalulty_level": "intermediate",
        "total_duration_in_seconds": 46800,
        "ispublished": False,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440009",
        "title": "Machine Learning",
        "subtitle": "Introduction to machine learning",
        "description": "Learn machine learning fundamentals, data preparation, regression, classification, model evaluation, and basic algorithms.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440009",
        "price": 1999.00,
        "discount_price": 1699.00,
        "thumbnail": "https://example.com/ml.jpg",
        "promovideo": "https://example.com/ml-video",
        "difficalulty_level": "advanced",
        "total_duration_in_seconds": 54000,
        "ispublished": True,
    }),

    CourseModel.model_validate({
        "courseid": "650e8400-e29b-41d4-a716-446655440010",
        "title": "REST API Design",
        "subtitle": "Design clean and scalable APIs",
        "description": "Learn REST principles, HTTP methods, status codes, authentication, validation, pagination, and API best practices.",
        "instructorid": "750e8400-e29b-41d4-a716-446655440010",
        "price": 1199.00,
        "discount_price": 899.00,
        "thumbnail": "https://example.com/rest-api.jpg",
        "promovideo": "https://example.com/rest-api-video",
        "difficalulty_level": "intermediate",
        "total_duration_in_seconds": 30000,
        "ispublished": True,
    }),
]


# ============================================================
# User Database
# ============================================================

UserDB: list[UserModel] = [
    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440001",
        "name": "Arun Kumar",
        "email": "arun.kumar@example.com",
        "dob": "1998-05-12",
        "password": "Arun@1234",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440002",
        "name": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "dob": "1999-08-21",
        "password": "Priya@5678",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440003",
        "name": "Rahul Verma",
        "email": "rahul.verma@example.com",
        "dob": "1997-03-15",
        "password": "Rahul@9012",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440004",
        "name": "Sneha Reddy",
        "email": "sneha.reddy@example.com",
        "dob": "2000-11-08",
        "password": "Sneha@3456",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440005",
        "name": "Karan Mehta",
        "email": "karan.mehta@example.com",
        "dob": "1996-07-19",
        "password": "Karan@7890",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440006",
        "name": "Ananya Singh",
        "email": "ananya.singh@example.com",
        "dob": "2001-02-27",
        "password": "Ananya@2468",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440007",
        "name": "Rohit Patel",
        "email": "rohit.patel@example.com",
        "dob": "1995-12-03",
        "password": "Rohit@1357",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440008",
        "name": "Meera Nair",
        "email": "meera.nair@example.com",
        "dob": "1998-09-14",
        "password": "Meera@8642",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440009",
        "name": "Vikram Joshi",
        "email": "vikram.joshi@example.com",
        "dob": "1994-06-25",
        "password": "Vikram@9753",
    }),

    UserModel.model_validate({
        "userid": "750e8400-e29b-41d4-a716-446655440010",
        "name": "Divya Iyer",
        "email": "divya.iyer@example.com",
        "dob": "2002-01-17",
        "password": "Divya@4680",
    }),
]


# ============================================================
# User Comment Database
# ============================================================

UserCommentDB: list[UserCommentModel] = [
    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440001",
        "course_id": "650e8400-e29b-41d4-a716-446655440001",
        "user_id": "750e8400-e29b-41d4-a716-446655440001",
        "parent_comment": None,
        "content": "This course is really helpful!",
        "created_at": "2026-08-01",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440002",
        "course_id": "650e8400-e29b-41d4-a716-446655440001",
        "user_id": "750e8400-e29b-41d4-a716-446655440002",
        "parent_comment": "850e8400-e29b-41d4-a716-446655440001",
        "content": "I completely agree with you.",
        "created_at": "2026-08-02",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440003",
        "course_id": "650e8400-e29b-41d4-a716-446655440003",
        "user_id": "750e8400-e29b-41d4-a716-446655440003",
        "parent_comment": None,
        "content": "The explanations are very clear.",
        "created_at": "2026-08-03",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440004",
        "course_id": "650e8400-e29b-41d4-a716-446655440004",
        "user_id": "750e8400-e29b-41d4-a716-446655440004",
        "parent_comment": None,
        "content": "Can you explain this topic again?",
        "created_at": "2026-08-04",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440005",
        "course_id": "650e8400-e29b-41d4-a716-446655440004",
        "user_id": "750e8400-e29b-41d4-a716-446655440005",
        "parent_comment": "850e8400-e29b-41d4-a716-446655440004",
        "content": "Yes, I also found this part confusing.",
        "created_at": "2026-08-05",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440006",
        "course_id": "650e8400-e29b-41d4-a716-446655440006",
        "user_id": "750e8400-e29b-41d4-a716-446655440006",
        "parent_comment": None,
        "content": "The practical examples are excellent.",
        "created_at": "2026-08-06",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440007",
        "course_id": "650e8400-e29b-41d4-a716-446655440007",
        "user_id": "750e8400-e29b-41d4-a716-446655440007",
        "parent_comment": None,
        "content": "Very good course for beginners.",
        "created_at": "2026-08-07",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440008",
        "course_id": "650e8400-e29b-41d4-a716-446655440007",
        "user_id": "750e8400-e29b-41d4-a716-446655440008",
        "parent_comment": "850e8400-e29b-41d4-a716-446655440007",
        "content": "The first few lessons helped me a lot.",
        "created_at": "2026-08-08",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440009",
        "course_id": "650e8400-e29b-41d4-a716-446655440009",
        "user_id": "750e8400-e29b-41d4-a716-446655440009",
        "parent_comment": None,
        "content": "I would recommend this course.",
        "created_at": "2026-08-09",
    }),

    UserCommentModel.model_validate({
        "commentid": "850e8400-e29b-41d4-a716-446655440010",
        "course_id": "650e8400-e29b-41d4-a716-446655440010",
        "user_id": "750e8400-e29b-41d4-a716-446655440010",
        "parent_comment": None,
        "content": "Looking forward to the next lesson.",
        "created_at": "2026-08-10",
    }),
]