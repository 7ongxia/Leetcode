class Solution:
    def dp(self, jug1, jug2) -> int:
        # Check
        if (jug1, jug2) in self.memo:
            return self.memo[(jug1, jug2)]
        else:
            if (jug1 + jug2) == self.target:
                self.memo[(jug1, jug2)] = True
                self.result = True
                return True
            else:
                self.memo[(jug1, jug2)] = False

        # Fill Only Jar 1
        if (self.jug1Cap, jug2) not in self.memo:
            self.memo[(self.jug1Cap, jug2)] = self.dp(self.jug1Cap, jug2)

        # Fill Only Jar 2
        if (jug1, self.jug2Cap) not in self.memo:
            self.memo[(jug1, self.jug2Cap)] = self.dp(jug1, self.jug2Cap)

        # Fill Both Jars
        if (self.jug1Cap, self.jug2Cap) not in self.memo:
            self.memo[(self.jug1Cap, self.jug2Cap)] = self.dp(
                self.jug1Cap, self.jug2Cap)

        # Empty Only Jar 1
        if (0, jug2) not in self.memo:
            self.memo[(0, jug2)] = self.dp(0, jug2)

        # Empty Only Jar 2
        if (jug1, 0) not in self.memo:
            self.memo[(jug1, 0)] = self.dp(jug1, 0)

        # Jar1 -> Jar2
        new_jug1 = jug1 - (self.jug2Cap - jug2)
        new_jug2 = jug1 + jug2
        if new_jug1 < 0:
            new_jug1 = 0
        if new_jug2 > self.jug2Cap:
            new_jug2 = self.jug2Cap
        if (new_jug1, new_jug2) not in self.memo:
            self.memo[(new_jug1, new_jug2)] = self.dp(new_jug1, new_jug2)

        # Jar2 -> Jar1
        new_jug2 = jug2 - (self.jug1Cap - jug1)
        new_jug1 = jug1 + jug2
        if new_jug2 < 0:
            new_jug2 = 0
        if new_jug1 > self.jug1Cap:
            new_jug1 = self.jug1Cap
        if (new_jug1, new_jug2) not in self.memo:
            self.memo[(new_jug1, new_jug2)] = self.dp(new_jug1, new_jug2)

    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity == 0:
            return True

        self.memo = {}
        self.result = False
        self.target = targetCapacity
        self.jug1Cap = jug1Capacity
        self.jug2Cap = jug2Capacity

        self.dp(0, 0)

        return self.result
