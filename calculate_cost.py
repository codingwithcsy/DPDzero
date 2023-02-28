import json

# Load the cost per unit per channel from cost.json
with open('cost.json') as f:
    cost_data = json.load(f)

# Load the number of times each channel is used at a given time from channel-cost.json
with open('channel-cost.json') as f:
    channel_data = json.load(f)

# Calculate the total cost per day for each channel
total_cost = {}
for channel, channel_usage in channel_data.items():
    for date, usage in channel_usage.items():
        if date not in total_cost:
            total_cost[date] = {}
        if channel not in total_cost[date]:
            total_cost[date][channel] = 0
        total_cost[date][channel] += usage * cost_data[channel]

# Convert the total cost from paisa to rupees
for date, date_cost in total_cost.items():
    for channel, channel_cost in date_cost.items():
        total_cost[date][channel] = channel_cost / 100

# Write the total cost to a file
with open('total_cost.json', 'w') as f:
    json.dump(total_cost, f, sort_keys=True, indent=4)
