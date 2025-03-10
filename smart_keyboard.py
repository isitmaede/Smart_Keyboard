import tkinter as tk
import random

# نموذج مبسط للتنبؤ بالكلمات (يمكن ربطه بنموذج AI متطور لاحقًا)
word_predictions = {
    "مرحبا": ["بك", "كيف", "عزيزي", "أهلاً"],
    "أنا": ["أحب", "أريد", "أتعلم", "موجود"],
    "أحب": ["البرمجة", "الذكاء الصناعي", "الروبوتات", "Python"],
    "كيف": ["حالكم", "يمكن", "أقوم", "أتعلم"]
}

def predict_word():
    text = entry.get()
    last_word = text.split(" ")[-1] if text else ""
    predictions = word_predictions.get(last_word, ["..."])
    prediction_label.config(text=" | ".join(predictions))

# إنشاء واجهة المستخدم
root = tk.Tk()
root.title("⌨️ لوحة المفاتيح الذكية")
root.geometry("400x200")

tk.Label(root, text="📝 اكتب هنا:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=5)
entry.bind("<KeyRelease>", lambda event: predict_word())

prediction_label = tk.Label(root, text="🔮 الاقتراحات ستظهر هنا", font=("Arial", 12), fg="blue")
prediction_label.pack(pady=10)

root.mainloop()
