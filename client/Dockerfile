FROM node:16-alpine as build-deps
ENV GENERATE_SOURCEMAP false
ENV BASE_URL hello.world
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . ./
RUN npm run build

# Stage 2 - the production environment
FROM nginx:1.21.0-alpine
ENV GENERATE_SOURCEMAP false
ENV BASE_URL hello.world
COPY --from=build-deps /usr/src/app/dist /usr/share/nginx/html

COPY dev.default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]