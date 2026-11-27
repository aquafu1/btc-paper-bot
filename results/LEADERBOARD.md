# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1552 windows, 38120 settled trades, 421 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 788 | 34.3 | 35.3 | $-613.30 | -7.8% | $386.70 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3779 | 50.9 | 50.0 | $-972.87 | -2.6% | $27.13 | -1.6 | done | can't tell from luck |
| value_ev10 | 1878 | 38.4 | 39.1 | $-1033.95 | -5.5% | $-33.95 | -1.9 | done | can't tell from luck |
| value_ev5 | 2823 | 40.5 | 41.0 | $-1437.60 | -5.1% | $-437.60 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3171 | 51.0 | 50.9 | $-1521.62 | -4.8% | $-521.62 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3171 | 49.0 | 49.2 | $-1657.89 | -5.2% | $-657.89 | -2.9 | done | losing for real |
| trend_filter | 2249 | 48.6 | 50.3 | $-1924.37 | -8.6% | $-924.37 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3779 | 49.1 | 50.2 | $-2345.81 | -6.2% | $-1345.81 | -3.8 | done | losing for real |
| coinflip | 5494 | 49.9 | 49.9 | $-2417.61 | -4.4% | $-1417.61 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5494 | 50.2 | 51.3 | $-3396.74 | -6.2% | $-2396.74 | -4.7 | done | losing for real |
| always_up | 5494 | 48.2 | 49.2 | $-3548.21 | -6.5% | $-2548.21 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10017 | 47.9 | 48.7 | $-5756.83 |
| ETH | 10793 | 48.1 | 47.8 | $-5528.90 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
