# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 106 windows, 2709 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 205 | 60.0 | 53.1 | $+208.20 | +10.2% | $1208.20 | +1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 262 | 55.3 | 52.1 | $+100.95 | +3.9% | $1100.95 | +0.6 | done | can't tell from luck |
| momentum_5m_0.00pct | 416 | 52.9 | 50.8 | $+3.74 | +0.1% | $1003.74 | +0.0 | done | can't tell from luck |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 9:15 AM | too few trades (50/200) |
| value_ev10 | 140 | 38.6 | 40.6 | $-129.31 | -9.2% | $870.69 | -0.9 | Thu 8:00 AM | too few trades (140/200) |
| trend_filter | 144 | 42.4 | 49.0 | $-238.60 | -16.6% | $761.40 | -2.0 | Thu 7:00 AM | too few trades (144/200) |
| coinflip | 416 | 49.8 | 51.3 | $-292.38 | -7.0% | $707.62 | -1.5 | done | can't tell from luck |
| value_ev5 | 193 | 36.3 | 41.9 | $-323.38 | -16.8% | $676.62 | -2.1 | Wed 9:00 PM | too few trades (193/200) |
| momentum_15m_0.10pct | 262 | 44.7 | 50.0 | $-365.70 | -14.0% | $634.30 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 205 | 40.0 | 48.9 | $-431.39 | -21.0% | $568.61 | -3.0 | done | losing for real |
| always_up | 416 | 46.9 | 50.3 | $-440.97 | -10.6% | $559.03 | -2.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 584 | 45.4 | 49.6 | $-561.15 |
| ETH | 661 | 45.7 | 48.9 | $-633.25 |
| SOL | 723 | 48.3 | 48.5 | $-509.26 |
| XRP | 741 | 50.2 | 49.1 | $-329.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
