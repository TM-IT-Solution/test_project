import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import javax.security.auth.login.LoginException;

public class SimpleBot extends ListenerAdapter {

    public static void main(String[] args) throws LoginException {
        JDABuilder.createDefault("YOUR_BOT_TOKEN")
                .addEventListeners(new SimpleBot())
                .build();
    }

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {
        if (event.getAuthor().isBot()) return; // Ignore messages from other bots

        String[] args = event.getMessage().getContentRaw().split("\\s+");
        if (args[0].equalsIgnoreCase("!ping")) {
            event.getChannel().sendMessage("Pong!").queue();
        } else if (args[0].equalsIgnoreCase("!hello")) {
            event.getChannel().sendMessage("Hello!").queue();
        }
    }
}

