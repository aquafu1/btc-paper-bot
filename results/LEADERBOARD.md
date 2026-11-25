# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 11:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1356 windows, 35481 settled trades, 395 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 700 | 34.1 | 35.4 | $-561.96 | -8.0% | $438.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1714 | 38.6 | 39.2 | $-873.70 | -5.1% | $126.30 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3545 | 50.9 | 50.1 | $-1021.74 | -2.9% | $-21.74 | -1.7 | done | can't tell from luck |
| value_ev5 | 2588 | 40.4 | 41.1 | $-1365.69 | -5.3% | $-365.69 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2983 | 49.3 | 49.4 | $-1482.49 | -5.0% | $-482.49 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2983 | 50.7 | 50.9 | $-1539.88 | -5.2% | $-539.88 | -2.9 | done | losing for real |
| trend_filter | 2111 | 48.5 | 50.4 | $-1879.16 | -8.9% | $-879.16 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3545 | 49.1 | 50.3 | $-2241.11 | -6.3% | $-1241.11 | -3.8 | done | losing for real |
| coinflip | 5104 | 50.0 | 50.1 | $-2295.49 | -4.5% | $-1295.49 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5104 | 50.2 | 51.3 | $-3140.28 | -6.2% | $-2140.28 | -4.5 | done | losing for real |
| always_up | 5104 | 47.8 | 49.3 | $-3743.05 | -7.3% | $-2743.05 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8745 | 47.8 | 48.8 | $-5389.66 |
| ETH | 9426 | 48.1 | 48.2 | $-5170.68 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
