from dataclasses import dataclass


def group_pairs(pairs: set[tuple[int, int]]) -> list[set[int]]:
    groups = []
    for a, b in pairs:
        found = []
        for group in groups:
            if a in group or b in group:
                found.append(group)

        if found:
            merged = set.union(*found, {a, b})
            groups = [g for g in groups if g not in found]
            groups.append(merged)
        else:
            groups.append({a, b})

    return groups


@dataclass(frozen=True)
class Plot:
    x: int
    y: int
    v: str


class Grid:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.col_count = len(self.grid[0])
        self.row_count = len(self.grid)

    def _inbound(self, x: int, y: int):
        return 0 <= x < self.col_count and 0 <= y < self.row_count

    def _neighbors(self, x: int, y: int) -> list[Plot]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [
            Plot(nx, ny, self.grid[ny][nx])
            for dx, dy in directions
            if self._inbound((nx := x + dx), (ny := y + dy))
        ]

    def _perimeter(self, plot: Plot) -> int:
        return 4 - len([n for n in self._neighbors(plot.x, plot.y) if n.v == plot.v])

    def _build_regions(self) -> dict[int, list[Plot]]:
        region_id = 0
        assigned_plots: dict[Plot, int] = {}
        # first pass
        for j in range(self.row_count):
            for i in range(self.col_count):
                p = Plot(i, j, self.grid[j][i])
                neighbors = self._neighbors(p.x, p.y)
                if p in assigned_plots:
                    continue
                for n in neighbors:
                    if n in assigned_plots and n.v == p.v:
                        assigned_plots[p] = assigned_plots[n]
                if not p in assigned_plots:
                    region_id += 1
                    assigned_plots[p] = region_id
                    for n in neighbors:
                        if not n in assigned_plots and n.v == p.v:
                            assigned_plots[n] = region_id

        # merge regions
        regions_to_merge: set[tuple[int, int]] = set()
        for p in assigned_plots:
            neighbors = self._neighbors(p.x, p.y)
            for n in neighbors:
                if n.v == p.v and n in assigned_plots and assigned_plots[n] != assigned_plots[p]:
                    regions_to_merge.add((assigned_plots[n], assigned_plots[p]))

        regions_groups_to_merge = group_pairs(regions_to_merge)

        regions: dict[int, list[Plot]] = {}
        for p, r in assigned_plots.items():
            regions.setdefault(r, []).append(p)

        for g in regions_groups_to_merge:
            sg = sorted(g)
            r1 = sg[0]
            for r2 in sg[1:]:
                regions[r1].extend(regions[r2])
                del regions[r2]

        return regions

    def total_price(self) -> int:
        regions = self._build_regions()
        t = 0
        for _, plots in regions.items():
            area = len(plots)
            perimeter = sum(self._perimeter(p) for p in plots)
            print(plots[0].v, area, perimeter)
            t += area * perimeter
        return t

    def pprint(self):
        for row in self.grid:
            print("".join(row))


if __name__ == '__main__':
    with open('input/day12.txt', 'r') as xs:
        grid = Grid([list(line.strip()) for line in xs.readlines()])

    print(grid.total_price())
