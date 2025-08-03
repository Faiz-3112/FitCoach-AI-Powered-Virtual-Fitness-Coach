def calculate_macros(weight, goal, activity_level):
    activity_map = {'Low': 1.2, 'Medium': 1.4, 'High': 1.6}
    split_map = {
        "Fat Loss": {'cal': 22, 'split': (0.40, 0.35, 0.25)},
        "Maintenance": {'cal': 24, 'split': (0.30, 0.45, 0.25)},
        "Muscle Gain": {'cal': 26, 'split': (0.30, 0.50, 0.20)}
    }
    cal_factor = split_map[goal]['cal']
    multiplier = activity_map[activity_level]
    total_cal = weight * cal_factor * multiplier
    protein_pct, carb_pct, fat_pct = split_map[goal]['split']
    protein_g = (total_cal * protein_pct) / 4
    carb_g = (total_cal * carb_pct) / 4
    fat_g = (total_cal * fat_pct) / 9
    return "Calories: %d kcal | Protein: %d g | Carbs: %d g | Fat: %d g" % (
        int(total_cal), int(protein_g), int(carb_g), int(fat_g)
    )
