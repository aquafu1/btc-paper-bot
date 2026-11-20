# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 937 windows, 25933 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1171 | 37.9 | 39.1 | $-713.12 | -6.1% | $286.88 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2651 | 51.0 | 50.6 | $-871.41 | -3.3% | $128.59 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2216 | 50.1 | 49.9 | $-947.59 | -4.3% | $52.41 | -2.0 | done | losing for real |
| trend_filter | 1542 | 50.0 | 51.0 | $-1063.55 | -6.9% | $-63.55 | -2.8 | done | losing for real |
| value_ev5 | 1781 | 39.6 | 41.0 | $-1169.62 | -6.6% | $-169.62 | -2.3 | done | losing for real |
| coinflip | 3743 | 50.4 | 50.4 | $-1544.34 | -4.1% | $-544.34 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2216 | 49.9 | 50.9 | $-1545.45 | -7.0% | $-545.45 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2651 | 49.0 | 50.3 | $-1734.37 | -6.5% | $-734.37 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3743 | 51.0 | 51.6 | $-1914.40 | -5.1% | $-914.40 | -3.2 | done | losing for real |
| always_up | 3743 | 46.7 | 49.7 | $-3860.46 | -10.3% | $-2860.46 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5905 | 48.1 | 49.1 | $-3491.14 |
| ETH | 6450 | 48.2 | 48.6 | $-4090.89 |
| SOL | 6768 | 48.2 | 48.6 | $-3997.54 |
| XRP | 6810 | 48.3 | 48.5 | $-3940.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
