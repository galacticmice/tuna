"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fastify_1 = __importDefault(require("fastify"));
const PORT = 3000;
// remove pino-pretty in production
const fastify = (0, fastify_1.default)({ logger: { transport: { target: "pino-pretty" } } });
fastify.get('/', (request, response) => {
    return response.status(200).send({ message: "HELLO! You've caught tuna!" });
});
// server start
async function main() {
    try {
        await fastify.listen({ port: PORT });
        console.log(`Server listening at ${PORT}`);
    }
    catch (error) {
        fastify.log.error(error);
        process.exit(1);
    }
}
// shutdown
["SIGINT", "SIGTERM"].forEach((signal) => {
    process.on(signal, async () => {
        await fastify.close();
        process.exit(0);
    });
});
main();
