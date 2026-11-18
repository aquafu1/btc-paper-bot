# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 4:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 705 windows, 19456 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 372 | 34.1 | 34.9 | $-244.03 | -6.6% | $755.97 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1634 | 50.2 | 49.4 | $-502.57 | -3.1% | $497.43 | -1.2 | done | can't tell from luck |
| value_ev10 | 901 | 38.3 | 39.1 | $-533.27 | -5.9% | $466.73 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1995 | 51.6 | 50.8 | $-551.68 | -2.8% | $448.32 | -1.2 | done | can't tell from luck |
| trend_filter | 1133 | 50.3 | 50.9 | $-615.44 | -5.4% | $384.56 | -1.9 | done | can't tell from luck |
| value_ev5 | 1356 | 40.8 | 41.1 | $-625.25 | -4.6% | $374.75 | -1.4 | done | can't tell from luck |
| coinflip | 2812 | 50.2 | 50.3 | $-1196.41 | -4.3% | $-196.41 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1634 | 49.8 | 51.4 | $-1240.27 | -7.6% | $-240.27 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1995 | 48.4 | 50.0 | $-1397.53 | -7.0% | $-397.53 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2812 | 51.0 | 51.8 | $-1426.78 | -5.1% | $-426.78 | -2.8 | done | losing for real |
| always_up | 2812 | 47.4 | 49.6 | $-2385.69 | -8.5% | $-1385.69 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4412 | 48.2 | 49.1 | $-2576.36 |
| ETH | 4840 | 48.3 | 48.5 | $-2763.25 |
| SOL | 5077 | 48.3 | 48.7 | $-2861.37 |
| XRP | 5127 | 48.6 | 48.4 | $-2517.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
