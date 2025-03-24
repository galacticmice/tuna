import Fastify from 'fastify';

const PORT = 3000;

// remove pino-pretty in production
const fastify = Fastify({
    logger: {
        transport: {
            target: "pino-pretty"
        }
    }});

fastify.get('/', (request, response) => {
    return response.status(200).send({message: "HELLO!"});
})

async function main() {
    try {
        await fastify.listen({port: PORT})
        console.log(`Server listening at ${PORT}`)
    } catch (error) {
        fastify.log.error(error);
        process.exit(1);
    }
}

["SIGINT", "SIGTERM"].forEach((signal) => {
    process.on(signal, async () => {
        await fastify.close();
        process.exit(0);
    })
})

main();