# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 625 windows, 17284 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1462 | 51.3 | 49.5 | $-137.87 | -0.9% | $862.13 | -0.4 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 1001 | 50.2 | 50.8 | $-541.18 | -5.4% | $458.82 | -1.7 | done | can't tell from luck |
| value_ev10 | 799 | 38.3 | 39.5 | $-574.31 | -7.2% | $425.69 | -1.7 | done | can't tell from luck |
| value_ev5 | 1209 | 40.6 | 41.4 | $-719.30 | -5.9% | $280.70 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1770 | 50.8 | 51.1 | $-826.20 | -4.7% | $173.80 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1770 | 49.2 | 49.9 | $-974.04 | -5.5% | $25.96 | -2.3 | done | losing for real |
| coinflip | 2494 | 50.0 | 50.5 | $-1230.11 | -4.9% | $-230.11 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1462 | 48.7 | 51.4 | $-1440.42 | -9.9% | $-440.42 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2494 | 50.3 | 51.7 | $-1560.18 | -6.3% | $-560.18 | -3.2 | done | losing for real |
| always_up | 2494 | 47.5 | 49.7 | $-2117.50 | -8.5% | $-1117.50 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3927 | 48.2 | 49.2 | $-2422.77 |
| ETH | 4330 | 48.2 | 48.6 | $-2643.03 |
| SOL | 4487 | 47.9 | 48.8 | $-3007.06 |
| XRP | 4540 | 48.5 | 48.5 | $-2312.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
