# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 4:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1280 windows, 34349 settled trades, 417 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 674 | 34.0 | 35.3 | $-550.36 | -8.2% | $449.64 | -1.6 | done | can't tell from luck |
| value_ev10 | 1649 | 38.6 | 39.2 | $-850.65 | -5.2% | $149.35 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3445 | 50.7 | 50.2 | $-1191.89 | -3.5% | $-191.89 | -2.0 | done | losing for real |
| value_ev5 | 2492 | 40.4 | 41.1 | $-1302.01 | -5.2% | $-302.01 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2879 | 49.5 | 49.4 | $-1346.55 | -4.7% | $-346.55 | -2.5 | done | losing for real |
| trend_filter | 2033 | 49.0 | 50.5 | $-1623.73 | -8.0% | $-623.73 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2879 | 50.5 | 51.0 | $-1653.39 | -5.7% | $-653.39 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3445 | 49.3 | 50.3 | $-2058.38 | -6.0% | $-1058.38 | -3.5 | done | losing for real |
| coinflip | 4951 | 49.9 | 50.1 | $-2295.37 | -4.6% | $-1295.37 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4951 | 50.5 | 51.4 | $-2775.68 | -5.6% | $-1775.68 | -4.1 | done | losing for real |
| always_up | 4951 | 47.8 | 49.3 | $-3650.09 | -7.4% | $-2650.09 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8199 | 48.0 | 48.8 | $-4912.49 |
| ETH | 8840 | 48.2 | 48.2 | $-4801.37 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
