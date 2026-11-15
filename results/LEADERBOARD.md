# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 382 windows, 10404 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 9:30 PM | too few trades (196/200) |
| value_ev10 | 505 | 39.8 | 40.5 | $-237.29 | -4.7% | $762.71 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 869 | 49.8 | 49.7 | $-360.31 | -4.1% | $639.69 | -1.2 | done | can't tell from luck |
| value_ev5 | 745 | 41.5 | 42.1 | $-366.06 | -4.9% | $633.94 | -1.2 | done | can't tell from luck |
| trend_filter | 580 | 48.4 | 50.5 | $-487.94 | -8.4% | $512.06 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1040 | 51.6 | 52.1 | $-511.05 | -4.9% | $488.95 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1040 | 48.4 | 49.6 | $-638.66 | -6.1% | $361.34 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 869 | 50.2 | 52.1 | $-653.13 | -7.5% | $346.87 | -2.3 | done | losing for real |
| coinflip | 1520 | 50.0 | 50.8 | $-791.47 | -5.2% | $208.53 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1520 | 49.3 | 51.5 | $-1178.11 | -7.8% | $-178.11 | -3.1 | done | losing for real |
| always_up | 1520 | 45.7 | 50.8 | $-2040.88 | -13.4% | $-1040.88 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2344 | 47.3 | 49.4 | $-1862.31 |
| ETH | 2614 | 47.6 | 48.9 | $-1879.67 |
| SOL | 2696 | 47.8 | 49.4 | $-2046.75 |
| XRP | 2750 | 48.5 | 49.1 | $-1503.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
