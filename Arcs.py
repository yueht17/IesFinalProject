INF = 2 ** 31
arcs = {
    "arc_1": {
        "from": "1",
        "to": "6",
        "capacity": 8,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_2": {
        "from": "1",
        "to": "7",
        "capacity": 4,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_3": {
        "from": "1",
        "to": "8",
        "capacity": 9,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_4": {
        "from": "2",
        "to": "8",
        "capacity": 13,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_5": {
        "from": "2",
        "to": "9",
        "capacity": 7,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_6": {
        "from": "2",
        "to": "10",
        "capacity": 6,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_7": {
        "from": "3",
        "to": "10",
        "capacity": 5,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_8": {
        "from": "3",
        "to": "11",
        "capacity": 12,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_9": {
        "from": "3",
        "to": "12",
        "capacity": 7,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_10": {
        "from": "4",
        "to": "13",
        "capacity": 8,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_11": {
        "from": "4",
        "to": "14",
        "capacity": 15,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_12": {
        "from": "5",
        "to": "15",
        "capacity": 8,
        "fail_rate": 0.01,
        "maintain_cost": 4
    },
    "arc_13": {
        "from": "6",
        "to": "16",
        "capacity": 10,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_14": {
        "from": "7",
        "to": "16",
        "capacity": 4,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_15": {
        "from": "8",
        "to": "16",
        "capacity": 7,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_16": {
        "from": "9",
        "to": "17",
        "capacity": 10,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_17": {
        "from": "10",
        "to": "17",
        "capacity": 11,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_18": {
        "from": "11",
        "to": "17",
        "capacity": 13,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_19": {
        "from": "12",
        "to": "17",
        "capacity": 13,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_20": {
        "from": "13",
        "to": "18",
        "capacity": 13,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_21": {
        "from": "14",
        "to": "18",
        "capacity": 4,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_22": {
        "from": "15",
        "to": "18",
        "capacity": 9,
        "fail_rate": 0.02,
        "maintain_cost": 5
    },
    "arc_23": {
        "from": "3",
        "to": "2",
        "capacity": 15,
        "fail_rate": 0.15,
        "maintain_cost": 6
    },
    "arc_24": {
        "from": "3",
        "to": "4",
        "capacity": 9,
        "fail_rate": 0.15,
        "maintain_cost": 6
    },
    "arc_s1": {
        "from": "s",
        "to": "1",
        "capacity": INF,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
    "arc_s2": {
        "from": "s",
        "to": "3",
        "capacity": INF,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
    "arc_s3": {
        "from": "s",
        "to": "5",
        "capacity": INF,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
    "arc_s4": {
        "from": "s",
        "to": "2",
        "capacity": INF,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
    "arc_s5": {
        "from": "s",
        "to": "4",
        "capacity": INF,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
    "arc_d1": {
        "from": "16",
        "to": "d",
        "capacity": 15,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
    "arc_d2": {
        "from": "17",
        "to": "d",
        "capacity": 11,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
    "arc_d3": {
        "from": "18",
        "to": "d",
        "capacity": 14,
        "fail_rate": 0.0,
        "maintain_cost": 0
    },
}
