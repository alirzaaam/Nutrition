from django.shortcuts import render
import ollama

client = ollama.Client()

model_name = "dietplanpro"



# Create your views here.
def index(request):
    if request.method == "POST":
        gender = request.POST.get("gender_input")
        age = request.POST.get("age_input")
        height = request.POST.get("height_input")
        weight = request.POST.get("weight_input")
        activity = request.POST.get("activity")
        goal = request.POST.get("goal")
        preference = request.POST.get("preference")
        prompt = f"""
            Hello! I would like a personalized weight-loss diet plan.

            Here are my details:
            - Gender: {gender}
            - Age: {age}
            - Height: {height} cm
            - Weight: {weight} kg
            - Activity level: {activity}
            - Weight-loss goal: {goal}
            - Dietary preferences: {preference}

            Please provide:
            1. Daily calorie target range
            2. Full-day meal plan with calories for each item and meal totals
            3. Snack options with calories
            4. Daily total calories
            5. Hydration recommendations
            6. Optional safe workout pairing
            7. Weekly grocery list
            """
        response = client.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
        data = response["message"]["content"]
        # print(data)
        # print(activity)
        # print(goal)
        print(preference)
        return render(request, "diet_app/index.html", {
            "data":data})
    else:
        return render(request, "diet_app/index.html")
    
def test(request):
    return render(request, "diet_app/test.html")