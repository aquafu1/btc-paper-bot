# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 374 windows, 10158 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 195 | 37.4 | 36.5 | $-16.95 | -0.9% | $983.05 | -0.1 | Sat 8:00 PM | too few trades (195/200) |
| value_ev10 | 496 | 40.3 | 40.4 | $-169.12 | -3.4% | $830.88 | -0.6 | done | can't tell from luck |
| value_ev5 | 731 | 42.0 | 42.1 | $-272.45 | -3.7% | $727.55 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 843 | 49.8 | 49.7 | $-350.20 | -4.2% | $649.80 | -1.2 | done | can't tell from luck |
| trend_filter | 562 | 48.9 | 50.4 | $-420.47 | -7.5% | $579.53 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1012 | 51.7 | 52.1 | $-495.28 | -4.9% | $504.72 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1012 | 48.3 | 49.6 | $-627.29 | -6.2% | $372.71 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 843 | 50.2 | 52.1 | $-641.10 | -7.6% | $358.90 | -2.3 | done | losing for real |
| coinflip | 1488 | 49.8 | 50.8 | $-838.09 | -5.6% | $161.91 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1488 | 49.5 | 51.5 | $-1100.16 | -7.4% | $-100.16 | -3.0 | done | losing for real |
| always_up | 1488 | 45.6 | 50.8 | $-2034.53 | -13.7% | $-1034.53 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2287 | 47.3 | 49.3 | $-1851.52 |
| ETH | 2555 | 47.6 | 48.8 | $-1821.63 |
| SOL | 2631 | 47.9 | 49.4 | $-1950.50 |
| XRP | 2685 | 48.8 | 49.1 | $-1341.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
