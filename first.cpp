#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

typedef long int lint;

typedef vector<pair<lint, lint>>::iterator vec_iter;

double distance(const pair<lint, lint>& x, const pair<lint, lint>& y) {
    /**
    Calculates the manhattan distance between two points

    @param x pair<lint, lint> The first point on 2d.
    @param y pair<lint, lint> The second point on 2d.
    @return manhattan distance between point x and point y.
    */
    return abs(x.first - y.first) + abs(x.second - y.second);
}

double distance(const lint& greatest, const lint& smallest) {
    return greatest - smallest;
}

bool sortbysec(const pair<int,int> &a, const pair<int,int> &b) {
    /* Function used to sort a vector of pairs based on the second element */
    return (a.second < b.second);
}

double getYLine(const vec_iter& x_start, const lint& n){
    return ((x_start+(n/2)-1)->first + (x_start+(n/2))->first) / 2.;
}

double mergeSides(const vec_iter& x_begin, const vec_iter& x_end, const lint& n, const double& min_d) {
    double y = getYLine(x_begin, n);
    lint counter = 0;
    double min_new = min_d;
    for (vec_iter i = x_begin+(n/2); i < x_end; i++){
        if (distance(i->first, y) > min_d){
            break;
        }
        counter++;
    }
    vector<pair<lint, lint>> x(x_begin, x_end);
    sort(x.begin()+(n/2), x.begin()+(n/2)+counter, sortbysec);
    double upper, lower;
    double buffer;
    for (int i = (n/2)-1; i >= 0; i--){
        if (distance(y, x[i].first) > min_d){
            break;
        }
        upper = x[i].second + min_d;
        lower = x[i].second - min_d;
        vec_iter start = partition_point(x.begin()+(n/2), x.begin()+(n/2)+counter, [&lower](const pair<int, int>& box) -> 
        bool { return box.second < lower; });
        for (vec_iter j = start; j < x.begin()+(n/2)+counter; j++){
            if (j->second > upper) {
                break;
            }
            buffer = distance(x[i], *j);
            if (buffer < min_new){
                min_new = buffer;
            }
        }
    }
    return min_new;
}

double min_distance(const vec_iter& begin, const vec_iter& end) {
    double min_distance = HUGE_VAL;
    double current_distance;
    for (vec_iter i = begin; i < end; i++){
        for (vec_iter j = i+1; j < end; j++){
            current_distance = distance(*i, *j);
            if (min_distance > current_distance)
                min_distance = current_distance;
        }
    }

    return min_distance;
}

double closestDistance(const vec_iter& start, const vec_iter& finish, const int& n) {
    if (n < 4) {
        return min_distance(start, finish);
    } else {
        double d_i = closestDistance(start, start+(n/2), n/2);
        double d_d = closestDistance(start+(n/2), finish, ((n % 2) ? (n/2)+1 : n/2));
        double d = min(d_i, d_d);

        return mergeSides(start, finish, n, d);
    }
}

int main() {
    lint n, x, y;
    cin >> n;
    vector<pair<lint,lint>> points;
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        points.push_back(make_pair(x, y));
    }

    sort(points.begin(), points.end());

    cout << setprecision(20) << closestDistance(points.begin(), points.end() , n) << endl;
    return 0;
}
