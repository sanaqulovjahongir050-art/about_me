def wait_time_report(input_path, output_path, target_threshold):

    threshold = float(target_threshold)

    department_count = 0
    total_average_sum = 0

    best_department = ""
    best_average = None

    longest_department = ""
    longest_average = None

    within_target = 0

    report_lines = []

    with open(input_path, "r") as infile:

        for line in infile:

            line = line.strip()

            if line == "":
                continue

            parts = line.split("|")

            department = parts[0]

            wait_strings = parts[1].split(",")

            waits = []

            for value in wait_strings:
                waits.append(float(value))

            waits.sort()

            average = sum(waits) / len(waits)

            shortest = waits[0]
            longest = waits[-1]

            report_line = (
                f"{department}: "
                f"avg={average:.1f}min "
                f"shortest={shortest:.1f}min "
                f"longest={longest:.1f}min"
            )

            report_lines.append(report_line)

            department_count += 1
            total_average_sum += average

            if best_average is None or average < best_average:
                best_average = average
                best_department = department

            if longest_average is None or average > longest_average:
                longest_average = average
                longest_department = department

            if average <= threshold:
                within_target += 1

    hospital_average = total_average_sum / department_count

    with open(output_path, "w") as outfile:

        outfile.write("Patient Wait Time Report\n")
        outfile.write("==============================\n")

        for line in report_lines:
            outfile.write(line + "\n")

        outfile.write("\n")

        outfile.write(f"Hospital Average: {hospital_average:.1f} min\n")

        outfile.write(
            f"Best Dept:        "
            f"{best_department} ({best_average:.1f} min)\n"
        )

        outfile.write(
            f"Longest Wait:     "
            f"{longest_department} ({longest_average:.1f} min)\n"
        )

        outfile.write(
            f"Within Target ({int(threshold)}min): "
            f"{within_target}/{department_count}\n"
        )

    return {
        "departments": department_count,
        "hospital_avg": round(hospital_average, 1),
        "best": f"{best_department} ({best_average:.1f} min)",
        "longest": f"{longest_department} ({longest_average:.1f} min)",
        "within_target": within_target,
    }
