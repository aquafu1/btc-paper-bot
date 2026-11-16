# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 509 windows, 14032 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1190 | 51.0 | 49.8 | $-213.45 | -1.8% | $786.55 | -0.6 | done | can't tell from luck |
| value_ev10 | 659 | 38.1 | 39.7 | $-500.51 | -7.6% | $499.49 | -1.6 | done | can't tell from luck |
| trend_filter | 822 | 49.4 | 50.7 | $-570.35 | -6.9% | $429.65 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1422 | 49.6 | 49.6 | $-587.32 | -4.1% | $412.68 | -1.6 | done | can't tell from luck |
| value_ev5 | 976 | 40.0 | 41.5 | $-713.88 | -7.3% | $286.12 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1422 | 50.4 | 51.6 | $-940.64 | -6.6% | $59.36 | -2.6 | done | losing for real |
| coinflip | 2029 | 50.0 | 50.7 | $-1079.99 | -5.3% | $-79.99 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1190 | 49.0 | 51.4 | $-1082.95 | -9.1% | $-82.95 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2029 | 49.6 | 51.6 | $-1549.12 | -7.6% | $-549.12 | -3.6 | done | losing for real |
| always_up | 2029 | 46.3 | 50.1 | $-2384.90 | -11.8% | $-1384.90 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3179 | 47.3 | 49.2 | $-2568.15 |
| ETH | 3504 | 48.0 | 48.7 | $-2289.28 |
| SOL | 3656 | 47.6 | 49.0 | $-2794.00 |
| XRP | 3693 | 48.3 | 48.8 | $-2150.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
