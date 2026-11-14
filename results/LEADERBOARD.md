# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 362 windows, 9774 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 188 | 37.8 | 36.4 | $+2.39 | +0.1% | $1002.39 | +0.0 | Sat 8:45 PM | too few trades (188/200) |
| value_ev10 | 473 | 40.8 | 40.2 | $-87.57 | -1.9% | $912.43 | -0.3 | done | can't tell from luck |
| value_ev5 | 701 | 42.1 | 42.0 | $-229.07 | -3.3% | $770.93 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 970 | 51.9 | 52.1 | $-437.37 | -4.5% | $562.63 | -1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 803 | 51.1 | 52.0 | $-457.12 | -5.7% | $542.88 | -1.7 | done | can't tell from luck |
| trend_filter | 540 | 48.3 | 50.6 | $-470.88 | -8.7% | $529.12 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 803 | 48.9 | 49.7 | $-483.76 | -6.0% | $516.24 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 970 | 48.1 | 49.6 | $-641.88 | -6.6% | $358.12 | -2.1 | done | losing for real |
| coinflip | 1442 | 50.1 | 50.8 | $-713.20 | -4.9% | $286.80 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1442 | 49.5 | 51.5 | $-1072.43 | -7.4% | $-72.43 | -2.9 | done | losing for real |
| always_up | 1442 | 46.0 | 50.7 | $-1852.59 | -12.8% | $-852.59 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2196 | 47.3 | 49.3 | $-1737.49 |
| ETH | 2462 | 47.7 | 48.8 | $-1744.29 |
| SOL | 2531 | 48.1 | 49.4 | $-1770.98 |
| XRP | 2585 | 48.9 | 49.1 | $-1190.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
