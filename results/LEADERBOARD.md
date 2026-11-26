# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1511 windows, 37575 settled trades, 393 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 764 | 34.6 | 35.4 | $-548.45 | -7.2% | $451.55 | -1.5 | done | can't tell from luck |
| value_ev10 | 1835 | 38.6 | 39.2 | $-918.95 | -5.0% | $81.05 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3738 | 50.9 | 50.1 | $-957.90 | -2.6% | $42.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 2766 | 40.6 | 41.1 | $-1316.82 | -4.8% | $-316.82 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3136 | 51.1 | 51.0 | $-1424.29 | -4.5% | $-424.29 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3136 | 48.9 | 49.2 | $-1720.56 | -5.5% | $-720.56 | -3.1 | done | losing for real |
| trend_filter | 2226 | 48.6 | 50.3 | $-1912.55 | -8.6% | $-912.55 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3738 | 49.1 | 50.2 | $-2309.28 | -6.2% | $-1309.28 | -3.8 | done | losing for real |
| coinflip | 5412 | 50.0 | 50.0 | $-2379.36 | -4.4% | $-1379.36 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5412 | 50.2 | 51.3 | $-3304.85 | -6.1% | $-2304.85 | -4.6 | done | losing for real |
| always_up | 5412 | 48.0 | 49.2 | $-3561.84 | -6.6% | $-2561.84 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9757 | 48.0 | 48.7 | $-5357.99 |
| ETH | 10508 | 48.1 | 47.9 | $-5412.62 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
