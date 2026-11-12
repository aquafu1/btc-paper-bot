# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 106 windows, 2718 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 206 | 60.2 | 53.1 | $+215.81 | +10.5% | $1215.81 | +1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 263 | 55.1 | 52.0 | $+90.95 | +3.5% | $1090.95 | +0.6 | done | can't tell from luck |
| momentum_5m_0.00pct | 417 | 53.0 | 50.8 | $+11.35 | +0.3% | $1011.35 | +0.1 | done | can't tell from luck |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 10:15 AM | too few trades (50/200) |
| value_ev10 | 141 | 38.3 | 40.6 | $-139.31 | -9.9% | $860.69 | -1.0 | Thu 8:15 AM | too few trades (141/200) |
| trend_filter | 144 | 42.4 | 49.0 | $-238.60 | -16.6% | $761.40 | -2.0 | Thu 7:15 AM | too few trades (144/200) |
| coinflip | 417 | 49.9 | 51.3 | $-284.77 | -6.8% | $715.23 | -1.5 | done | can't tell from luck |
| value_ev5 | 194 | 36.1 | 41.9 | $-333.38 | -17.2% | $666.62 | -2.1 | Wed 9:00 PM | too few trades (194/200) |
| momentum_15m_0.10pct | 263 | 44.9 | 50.1 | $-358.09 | -13.6% | $641.91 | -2.2 | done | losing for real |
| always_up | 417 | 47.0 | 50.3 | $-433.36 | -10.4% | $566.64 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 206 | 39.8 | 48.9 | $-441.39 | -21.4% | $558.61 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 593 | 45.5 | 49.7 | $-563.11 |
| ETH | 661 | 45.7 | 48.9 | $-633.25 |
| SOL | 723 | 48.3 | 48.5 | $-509.26 |
| XRP | 741 | 50.2 | 49.1 | $-329.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
