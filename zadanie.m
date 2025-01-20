global n h;
n = input('Podaj n: ');
h = 2/n;

function result = e (i,x)
global n h;
if x >= h*(i - 2) & x < h*(i -1)
    result = (x - h*(i - 2))/h;
elseif x >= h*(i - 1) & x < h*(i)
    result = (h - (x - h*(i -1 )))/h;
else
    result = 0;

end
end

function result = e_prim(i,x)
global n h;
if x >= h*(i - 2) & x < h*(i -1)
    result = 1/h;
elseif x >= h*(i - 1) & x < h*(i)
    result = -1/h;
else
    result = 0;

end
end

function result = L(i)
global n h;
result = -37/2 * e(i,0) + 3/2 * e(i,1);
end

function result = k(x)
global n h;
if x <= 1 & x >= 0
    result = 1;
elseif x <= 2 & x > 1
    result = 2;
else
    result = 0;
end
end

function result = B(i,j)
global n h;
result = -2*e(j,2)*e_prim(i,2)-e(j,0)*e(i,0)+integral(@(x) k(x).*e_prim(i,x).*e_prim(j,x),0,2,'ArrayValued', true);
end

function result = u(W,x)
global n h;
result = 3/2*x;
for i = 1:n
    result = result + W(i)*e(i,x);
end
end

A = zeros(n, n);
for i = 1:n
    for j = 1:n
        A(i, j) = B(i, j);
    end
end

V = zeros(n, 1);
for i = 1:n
    V(i) = L(i);
end

W = A\V;

x_values = linspace(0, 2, 1000);
u_values = arrayfun(@(x) u(W, x), x_values);

figure;
plot(x_values, u_values);
xlabel('x');
ylabel('u(x)');
title('Plot of the function u(x)');
grid on;