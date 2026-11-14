# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 354 windows, 9536 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 7:45 PM | too few trades (186/200) |
| value_ev10 | 459 | 40.1 | 40.3 | $-196.10 | -4.3% | $803.90 | -0.8 | done | can't tell from luck |
| value_ev5 | 683 | 41.6 | 42.0 | $-336.09 | -4.9% | $663.91 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 946 | 52.1 | 52.1 | $-391.11 | -4.1% | $608.89 | -1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 781 | 51.3 | 52.0 | $-404.95 | -5.2% | $595.05 | -1.5 | done | can't tell from luck |
| trend_filter | 527 | 48.0 | 50.4 | $-480.19 | -9.1% | $519.81 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 781 | 48.7 | 49.7 | $-514.30 | -6.6% | $485.70 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 946 | 47.9 | 49.7 | $-723.86 | -7.7% | $276.14 | -2.4 | done | losing for real |
| coinflip | 1409 | 50.1 | 50.8 | $-736.52 | -5.2% | $263.48 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1409 | 49.5 | 51.5 | $-1073.28 | -7.6% | $-73.28 | -3.0 | done | losing for real |
| always_up | 1409 | 46.6 | 50.6 | $-1663.11 | -11.8% | $-663.11 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2143 | 47.3 | 49.3 | $-1750.48 |
| ETH | 2400 | 47.6 | 48.7 | $-1756.26 |
| SOL | 2469 | 48.1 | 49.4 | $-1805.40 |
| XRP | 2524 | 48.9 | 49.1 | $-1265.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
