# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 373 windows, 10147 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 194 | 37.6 | 36.6 | $-6.95 | -0.4% | $993.05 | -0.0 | Sat 8:30 PM | too few trades (194/200) |
| value_ev10 | 495 | 40.4 | 40.5 | $-159.12 | -3.2% | $840.88 | -0.6 | done | can't tell from luck |
| value_ev5 | 730 | 42.1 | 42.1 | $-262.45 | -3.6% | $737.55 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 842 | 49.9 | 49.7 | $-340.20 | -4.0% | $659.80 | -1.2 | done | can't tell from luck |
| trend_filter | 561 | 49.0 | 50.5 | $-410.47 | -7.3% | $589.53 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1011 | 51.6 | 52.1 | $-499.00 | -4.9% | $501.00 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1011 | 48.4 | 49.6 | $-617.29 | -6.1% | $382.71 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 842 | 50.1 | 52.1 | $-644.82 | -7.7% | $355.18 | -2.3 | done | losing for real |
| coinflip | 1487 | 49.8 | 50.8 | $-841.81 | -5.7% | $158.19 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1487 | 49.6 | 51.5 | $-1090.16 | -7.3% | $-90.16 | -2.9 | done | losing for real |
| always_up | 1487 | 45.6 | 50.8 | $-2038.25 | -13.7% | $-1038.25 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2287 | 47.3 | 49.3 | $-1851.52 |
| ETH | 2555 | 47.6 | 48.8 | $-1821.63 |
| SOL | 2620 | 47.9 | 49.5 | $-1895.38 |
| XRP | 2685 | 48.8 | 49.1 | $-1341.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
