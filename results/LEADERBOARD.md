# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 373 windows, 10116 settled trades, 73 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 193 | 37.8 | 36.6 | $+3.05 | +0.2% | $1003.05 | +0.0 | Sat 8:45 PM | too few trades (193/200) |
| value_ev10 | 492 | 40.7 | 40.5 | $-129.12 | -2.6% | $870.88 | -0.5 | done | can't tell from luck |
| value_ev5 | 727 | 42.2 | 42.1 | $-232.45 | -3.2% | $767.55 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 839 | 50.1 | 49.8 | $-310.20 | -3.7% | $689.80 | -1.1 | done | can't tell from luck |
| trend_filter | 558 | 49.3 | 50.6 | $-380.47 | -6.8% | $619.53 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1008 | 51.5 | 52.1 | $-513.27 | -5.1% | $486.73 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1008 | 48.5 | 49.7 | $-587.29 | -5.8% | $412.71 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 839 | 49.9 | 52.0 | $-659.09 | -7.9% | $340.91 | -2.4 | done | losing for real |
| coinflip | 1484 | 49.8 | 50.8 | $-826.67 | -5.6% | $173.33 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1484 | 49.7 | 51.6 | $-1060.16 | -7.1% | $-60.16 | -2.8 | done | losing for real |
| always_up | 1484 | 45.5 | 50.7 | $-2052.52 | -13.8% | $-1052.52 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2277 | 47.3 | 49.4 | $-1797.21 |
| ETH | 2544 | 47.7 | 48.9 | $-1754.16 |
| SOL | 2620 | 47.9 | 49.5 | $-1895.38 |
| XRP | 2675 | 48.8 | 49.1 | $-1301.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
