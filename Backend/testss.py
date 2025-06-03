import matplotlib.pyplot as plt

# List of Surah names in Qur’an order
surah_names = [
    "Al-Fatiha", "Al-Baqarah", "Al-Imran", "An-Nisa", "Al-Ma'idah", "Al-An'am", "Al-A'raf", "Al-Anfal",
    "At-Tawbah", "Yunus", "Hud", "Yusuf", "Ar-Ra'd", "Ibrahim", "Al-Hijr", "An-Nahl", "Al-Isra", "Al-Kahf",
    "Maryam", "Ta-Ha", "Al-Anbiya", "Al-Hajj", "Al-Mu'minun", "An-Nur", "Al-Furqan", "Ash-Shu'ara", "An-Naml",
    "Al-Qasas", "Al-Ankabut", "Ar-Rum", "Luqman", "As-Sajda", "Al-Ahzab", "Saba'", "Fatir", "Ya-Sin",
    "As-Saffat", "Sad", "Az-Zumar", "Ghafir", "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiya",
    "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf", "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar",
    "Ar-Rahman", "Al-Waqi'a", "Al-Hadid", "Al-Mujadila", "Al-Hashr", "Al-Mumtahana", "As-Saff", "Al-Jumu'a",
    "Al-Munafiqun", "At-Taghabun", "At-Talaq", "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Ma'arij",
    "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyamah", "Al-Insan", "Al-Mursalat", "An-Naba",
    "An-Nazi'at", "Abasa", "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj", "At-Tariq",
    "Al-A'la", "Al-Ghashiyah", "Al-Fajr", "Al-Balad", "Ash-Shams", "Al-Lail", "Adh-Dhuha", "Ash-Sharh", "At-Tin",
    "Al-Alaq", "Al-Qadr", "Al-Bayyina", "Az-Zalzalah", "Al-Adiyat", "Al-Qari'a", "At-Takathur", "Al-Asr",
    "Al-Humazah", "Al-Fil", "Quraysh", "Al-Ma'un", "Al-Kawthar", "Al-Kafirun", "An-Nasr", "Al-Masad", "Al-Ikhlas",
    "Al-Falaq", "An-Nas"
]

# Number of Ayat for each Surah in the same order
ayat_counts = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135, 112, 78, 118, 64, 77,
    227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62,
    55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19,
    36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 5, 4, 6
]

# Plotting the graph
plt.figure(figsize=(24, 6))
plt.plot(surah_names, ayat_counts, marker='o', linestyle='-', color='teal')
plt.xticks(rotation=90, fontsize=7)
plt.xlabel('Surah Name (in Qur’an order)')
plt.ylabel('Number of Ayat')
plt.title('Number of Ayat in Each Surah of the Qur’an')

plt.tight_layout()
plt.grid(True)
plt.show()
