# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 381 windows, 10384 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 9:30 PM | too few trades (196/200) |
| value_ev10 | 503 | 40.0 | 40.5 | $-217.29 | -4.3% | $782.71 | -0.8 | done | can't tell from luck |
| value_ev5 | 743 | 41.6 | 42.1 | $-346.06 | -4.7% | $653.94 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 867 | 49.7 | 49.7 | $-375.36 | -4.3% | $624.64 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1038 | 51.7 | 52.1 | $-491.05 | -4.7% | $508.95 | -1.6 | done | can't tell from luck |
| trend_filter | 578 | 48.3 | 50.5 | $-502.98 | -8.7% | $497.02 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 867 | 50.3 | 52.1 | $-633.13 | -7.3% | $366.87 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1038 | 48.3 | 49.6 | $-653.70 | -6.3% | $346.30 | -2.0 | done | losing for real |
| coinflip | 1518 | 49.9 | 50.8 | $-806.51 | -5.3% | $193.49 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1518 | 49.3 | 51.5 | $-1193.15 | -7.9% | $-193.15 | -3.2 | done | losing for real |
| always_up | 1518 | 45.8 | 50.8 | $-2020.88 | -13.3% | $-1020.88 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2334 | 47.3 | 49.4 | $-1853.54 |
| ETH | 2614 | 47.6 | 48.9 | $-1879.67 |
| SOL | 2686 | 47.8 | 49.4 | $-2030.72 |
| XRP | 2750 | 48.5 | 49.1 | $-1503.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
