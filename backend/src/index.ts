import Fastify from 'fastify';
const PORT = 8080;
const HOST = '0.0.0.0'

// remove pino-pretty in production
const fastify = Fastify({ logger: true });

fastify.get('/', (request, response) => {
    return response.status(200).send({message: "HELLO! You've caught tuna!"});
})



// server start
async function main() {
    try {
        await fastify.listen({port: PORT, host: HOST})
        console.log(`Server listening at ${PORT}`)
    } catch (error) {
        fastify.log.error(error);
        process.exit(1);
    }
}

// shutdown
["SIGINT", "SIGTERM"].forEach((signal) => {
    process.on(signal, async () => {
        await fastify.close();
        process.exit(0);
    })
})

main();