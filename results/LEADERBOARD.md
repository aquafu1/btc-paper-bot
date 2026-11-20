# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 937 windows, 25909 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1171 | 37.9 | 39.1 | $-713.12 | -6.1% | $286.88 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2648 | 51.0 | 50.6 | $-885.27 | -3.3% | $114.73 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2213 | 50.2 | 49.9 | $-934.77 | -4.2% | $65.23 | -2.0 | done | can't tell from luck |
| trend_filter | 1539 | 50.0 | 51.0 | $-1050.73 | -6.8% | $-50.73 | -2.8 | done | losing for real |
| value_ev5 | 1781 | 39.6 | 41.0 | $-1169.62 | -6.6% | $-169.62 | -2.3 | done | losing for real |
| coinflip | 3740 | 50.5 | 50.4 | $-1535.36 | -4.1% | $-535.36 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2213 | 49.8 | 50.9 | $-1559.31 | -7.0% | $-559.31 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2648 | 49.0 | 50.3 | $-1721.55 | -6.5% | $-721.55 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3740 | 51.0 | 51.6 | $-1901.57 | -5.1% | $-901.57 | -3.2 | done | losing for real |
| always_up | 3740 | 46.7 | 49.7 | $-3874.32 | -10.4% | $-2874.32 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5905 | 48.1 | 49.1 | $-3491.14 |
| ETH | 6442 | 48.2 | 48.6 | $-4079.42 |
| SOL | 6760 | 48.2 | 48.6 | $-4001.62 |
| XRP | 6802 | 48.3 | 48.5 | $-3929.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
