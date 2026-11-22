# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1112 windows, 30786 settled trades, 23 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 587 | 34.4 | 35.1 | $-371.05 | -6.3% | $628.95 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3104 | 51.3 | 50.4 | $-725.25 | -2.3% | $274.75 | -1.3 | done | can't tell from luck |
| value_ev10 | 1434 | 37.9 | 39.1 | $-946.74 | -6.6% | $53.26 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2613 | 49.7 | 49.4 | $-1120.46 | -4.3% | $-120.46 | -2.2 | done | losing for real |
| value_ev5 | 2173 | 39.9 | 41.0 | $-1330.55 | -6.1% | $-330.55 | -2.4 | done | losing for real |
| trend_filter | 1826 | 49.2 | 50.4 | $-1390.26 | -7.6% | $-390.26 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2613 | 50.3 | 51.1 | $-1653.70 | -6.3% | $-653.70 | -3.3 | done | losing for real |
| coinflip | 4444 | 50.4 | 50.2 | $-1733.67 | -3.9% | $-733.67 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3104 | 48.7 | 50.2 | $-2187.63 | -7.0% | $-1187.63 | -4.0 | done | losing for real |
| momentum_5m_0.00pct | 4444 | 50.6 | 51.4 | $-2424.97 | -5.5% | $-1424.97 | -3.7 | done | losing for real |
| always_up | 4444 | 47.5 | 49.3 | $-3564.27 | -8.0% | $-2564.27 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7047 | 48.4 | 49.0 | $-3583.40 |
| ETH | 7626 | 48.1 | 48.4 | $-4705.03 |
| SOL | 8014 | 48.1 | 48.4 | $-4517.33 |
| XRP | 8099 | 48.2 | 48.2 | $-4642.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
