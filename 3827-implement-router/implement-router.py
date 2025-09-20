import collections

class Router:
    def __init__(self, memoryLimit: int):
        """
        Initializes the Router with a fixed memory limit.
        """
        self.memoryLimit = memoryLimit
        self.packet_queue = collections.deque()  # A deque acts as our doubly-linked list for FIFO.
        self.packet_set = set()  # A set for O(1) duplicate checking.
        self.destination_map = collections.defaultdict(list)  # Maps destination to a list of timestamps.

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        """
        Adds a packet if it's not a duplicate and the memory limit isn't exceeded.
        """
        packet = (source, destination, timestamp)
        
        # Check for duplicates using the hash set.
        if packet in self.packet_set:
            return False

        # If adding a new packet exceeds the memory limit, remove the oldest.
        if len(self.packet_queue) == self.memoryLimit:
            oldest_packet = self.packet_queue.popleft()
            self.packet_set.remove(oldest_packet)
            
            # Remove the oldest packet's timestamp from the destination map.
            oldest_dest = oldest_packet[1]
            oldest_ts = oldest_packet[2]
            self.destination_map[oldest_dest].remove(oldest_ts)

        # Add the new packet to our data structures.
        self.packet_queue.append(packet)
        self.packet_set.add(packet)
        
        # Add the timestamp to the destination map, maintaining sorted order.
        self.destination_map[destination].append(timestamp)

        return True

    def forwardPacket(self) -> list[int]:
        """
        Forwards the next packet in FIFO order.
        """
        if not self.packet_queue:
            return []

        packet = self.packet_queue.popleft()
        self.packet_set.remove(packet)
        
        # Remove the forwarded packet's timestamp from the destination map.
        dest = packet[1]
        ts = packet[2]
        self.destination_map[dest].remove(ts)

        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        """
        Returns the number of packets for a specific destination and time range.
        """
        if destination not in self.destination_map:
            return 0
            
        timestamps = self.destination_map[destination]
        
        # Using binary search to find the start and end of the range.
        start_index = self._binary_search_start(timestamps, startTime)
        end_index = self._binary_search_end(timestamps, endTime)
        
        if start_index == -1 or end_index == -1:
            return 0
        
        return end_index - start_index + 1
        
    def _binary_search_start(self, arr, target):
        """
        Helper method to find the first occurrence of a value >= target.
        """
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

    def _binary_search_end(self, arr, target):
        """
        Helper method to find the last occurrence of a value <= target.
        """
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result