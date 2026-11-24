# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1299 windows, 34659 settled trades, 413 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 683 | 34.3 | 35.3 | $-516.32 | -7.6% | $483.68 | -1.5 | done | can't tell from luck |
| value_ev10 | 1671 | 38.8 | 39.2 | $-753.35 | -4.5% | $246.65 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3477 | 50.8 | 50.2 | $-1033.34 | -3.0% | $-33.34 | -1.7 | done | can't tell from luck |
| value_ev5 | 2520 | 40.5 | 41.1 | $-1241.03 | -4.9% | $-241.03 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2906 | 49.4 | 49.4 | $-1337.76 | -4.6% | $-337.76 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2906 | 50.6 | 51.0 | $-1601.56 | -5.5% | $-601.56 | -3.0 | done | losing for real |
| trend_filter | 2052 | 48.9 | 50.4 | $-1669.32 | -8.1% | $-669.32 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3477 | 49.2 | 50.3 | $-2168.35 | -6.2% | $-1168.35 | -3.7 | done | losing for real |
| coinflip | 4989 | 50.0 | 50.1 | $-2238.53 | -4.5% | $-1238.53 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4989 | 50.4 | 51.4 | $-2841.42 | -5.7% | $-1841.42 | -4.1 | done | losing for real |
| always_up | 4989 | 47.9 | 49.3 | $-3544.77 | -7.1% | $-2544.77 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8342 | 48.0 | 48.8 | $-4748.16 |
| ETH | 9007 | 48.3 | 48.2 | $-4613.35 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
