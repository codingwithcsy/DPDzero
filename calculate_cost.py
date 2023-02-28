import json

# Load the cost per unit per channel from cost.json
with open('cost.json') as f:
    cost_data = json.load(f)

# Load the number of times each channel is used at a given time from channel-cost.json
with open('channel-cost.json') as f:
    channel_data = json.load(f)

# Calculate the total cost per day for each channel
total_cost = []
for date, channel_usage in channel_data.items():
    cost_per_day = {"date": date}
    for channel, usage in channel_usage.items():
        cost_per_day[channel] = round(usage * cost_data[channel] / 100, 2)
    total_cost.append(cost_per_day)

# Write the total cost to a file
with open('total_cost.json', 'w') as f:
    json.dump(total_cost, f, indent=4)
